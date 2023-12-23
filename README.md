Reward:
  +10 - eat food  
  -10 - game over  
  0   - else  

Actions:
  [1, 0, 0] - straight
  [0, 1, 0] - turn right
  [0, 0, 1] - turn left

State (11 boolean values):
  [danger straight, danger right, danger left,
   direction left, direction right,
   direction up, direction down,

   food left, food right,
   food up, food down]

Model:
  predict an action given the state:

  Deep Q Learning:
    Initial Q value (= initial model)
    Repeat:
      Choose action (model.predict(state))
      Perform action
      Evaluate reward
      Update Q value (+ train model)


## Bellman Equation

The Bellman equation is a fundamental concept in reinforcement learning, representing the value of a state in terms of the immediate reward and the discounted value of the next state.

The Bellman equation for the state-value function is defined as:

\[ V(s) = R(s) + γ * MAX Q(s, a) \]

where:
- \( V(s) \) is the value of state \( s \),
- \( R(s) \) is the immediate reward in state \( s \),
- \( γ \) is the discount factor,
- \( Q(s, a) \) is the action-value function representing the expected return from taking action \( a \) in state \( s \).

In the case of the Q-value function, the Bellman equation is expressed as:

\[ Q(s, a) = R(s, a) + γ * MAX Q'(s', a') \]

where:
- \( Q(s, a) \) is the Q-value for taking action \( a \) in state \( s \),
- \( R(s, a) \) is the immediate reward for taking action \( a \) in state \( s \),
- \( s' \) is the next state after taking action \( a \).

This equation captures the recursive relationship between the value of a state and the values of its neig





