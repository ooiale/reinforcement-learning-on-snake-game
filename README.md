<details>
<summary><strong>Agent</strong></summary>

```python
- game
- model
</details>
<details>
<summary><strong>Training</strong></summary>
state = get_state(game)
action = get_move(state)
>>> model.predict()
reward, game_over, score = game.play_step(action)
new_state = get_state(game)
remember
model.train()
</details>
```

**Agent**

```python
- game
- model

state = get_state(game)
action = get_move(state)
>>> model.predict()
reward, game_over, score = game.play_step(action)
new_state = get_state(game)
remember
model.train()
