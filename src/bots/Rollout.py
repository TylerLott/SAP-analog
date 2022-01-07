from src.Team import Team
from src.Fight import Fight


def rollout(policy1, policy2):
    team1, team2 = Team(), Team()
    obs_right, p1 = team1.getState()
    obs_left, p2 = team2.getState()

    done = False
    total_reward = 0
    t = 0

    while not done:
        for _ in range(10):
            action_right = policy1.predict(obs_right)
            action_left = policy2.predict(obs_left)

            team1.setState(action_right * p1)
            team2.setState(action_left * p2)

            obs_right, p1 = team1.getState()
            obs_left, p2 = team2.getState()

        team1.endTurn()
        team2.endTurn()
        f = Fight(team1, team2)
        f.simulate()
        team1.nextTurn()
        team2.nextTurn()
        t += 1
        if not team1.alive:
            total_reward = 1
            done = True
        elif not team2.alive:
            total_reward = -1
            done = True
        if not team1.alive and not team2.alive:
            done = True
            total_reward = 0

    return total_reward, t
