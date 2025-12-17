from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='Swim', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='Cycle', duration=60, calories=500)
        Activity.objects.create(user=clark, type='Yoga', duration=50, calories=200)

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
        Workout.objects.create(name='Flight Training', description='Aerobic workout for flyers')

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=1000)
        Leaderboard.objects.create(user=steve, score=900)
        Leaderboard.objects.create(user=bruce, score=950)
        Leaderboard.objects.create(user=clark, score=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
