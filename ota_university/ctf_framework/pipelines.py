from slackclient import SlackClient
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import CTFSlackUser
from .models import UserProfile



def login_user(request, api_data):
    """
    Callback from Slack oAuth after successful authentication.

    :type api_data: Dict
    :param api_data: Data returned from Slack after successful auth.
    """
    if api_data['ok']:

        # Get Slack User's display name from Slack API using access token
        sc = SlackClient(api_data["access_token"])
        user_profile = sc.api_call("users.profile.get")["profile"]

        # If user has a display name, use that. Otherwise use real name,
        # which is used as the display name in Slack.
        display_name = user_profile['display_name_normalized'] or user_profile["real_name_normalized"]

        # Create a guaranteed unique and static django username from slack Team ID and User ID
        user, created = User.objects.get_or_create(
            username="{}:{}".format(api_data['team_id'], api_data['user_id'])
        )

        if user.is_active:
            slacker, _ = CTFSlackUser.objects.get_or_create(slacker=user)
            slacker.access_token = api_data.pop('access_token')
            slacker.extras = api_data
            slacker.display_name = display_name
            slacker.save()

        if created:
            request.created_user = user
            profile = UserProfile(user=user)
            profile.save()

        login(request, user)

    return request, api_data
