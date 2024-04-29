
import matplotlib.pyplot as plt

from nqueen import NQueensState

states = []
seen_ans = []
n = 0
while True:
    state = NQueensState.random_state(N=16)

    if state.conflicts() == 0 :
        if state.queens not in seen_ans:
            seen_ans.append(state.queens)
            states.append(state)
            print(state)
            if len(states) == 2:
                
                states[0].plot()
                states[1].plot()
                break
            print(len(states))
            n +=1


