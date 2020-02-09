# GPS Limitation
# Problem: a man is sick and must get medicine in order to get healthy again. He can do this by approving a meeting
# with his doctor first. However he does not have the doctor's phone number and he does not have a scheduled meeting.

# This problem cannot be solved with GPS because of the conflict that occurs when trying to get the doctor's number.
# In order to talk to the doctor, he must know the phone number, and the only way to get his phone number is to
# ask him for it, but that means he must be talking with the doctor, which he can only do if he knows the phone number,
# thus an impossible problem.

# In real life a person would realize this conflict, so instead of giving up like GPS, they would expand their thoughts
# outside of their initial plan and could ask a friend for the doctor's number or look up the doctor's office phone
# number in a phone book. This demonstrates how the GPS is limited: it can only think along a given set of rules, so it
# is unable to predict/adapt to real world problems where things don't go as planned and unique solutions must be
# implemented.


from gps import gps


# Formulate the problem states and actions.
problem = {

    'initial': ['sick', 'no phone number', 'no meeting'],
    'goal': ['healthy'],

    'actions': [
        {
            'action': 'ask for doctor number',
            'preconds': ['talking with doctor'],
            'add': ['knows phone number'],
            'delete': ['no phone number']
        },
        {
            'action': 'talk to doctor',
            'preconds': ['knows phone number'],
            'add': ['approved meeting', 'talking with doctor'],
            'delete': ['no meeting']
        },
        {
            'action': 'get medicine',
            'preconds': ['approved meeting'],
            'add': ['healthy'],
            'delete': ['sick']
        }
    ]
}

if __name__ == '__main__':

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')