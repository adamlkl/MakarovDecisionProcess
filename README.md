# MakarovDecisionProcess

## Introduction ##
A **Markov decision process** (MDP) is a discrete time stochastic control process. It provides a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker. MDPs are useful for studying optimization problems solved via dynamic programming and reinforcement learning. They are used in many disciplines, including robotics, automatic control, economics and manufacturing.

At each time step, the process is in some state *s*, and the decision maker may choose any action *a* that is available in state *s*. The process responds at the next time step by randomly moving into a new state *s'*, and giving the decision maker a corresponding reward *R<sub>a</sub>(s,s′)*.

The probability that the process moves into its new state *s'* is influenced by the chosen action. Specifically, it is given by the state transition function *P<sub>a</sub>sub>(s,s′)*. Thus, the next state *s'* depends on the current state s and the decision maker's action *a*. But given *s* and *a*, it is conditionally independent of all previous states and actions. In other words, the state transitions of an MDP satisfies the Markov property.

## Running ##
To run the program, <br />
`python MDP.py n state gamma`
where n is the number of iterations,<br />      state is either fit, unfit or dead, <br />      gamma is any float number between 0 and 1.

## Test Results##
A sample of the test results can be found <a href="https://github.com/adamlkl/MarkovDecisionProcess/blob/master/Documentation/test_results.pdf">here</a>.

## Documentation ##
The assignment specifications can be found <a href="">here</a> or below.
<img src="https://github.com/adamlkl/MarkovDecisionProcess/blob/master/Documentation/0001.jpg" />
<img src="https://github.com/adamlkl/MarkovDecisionProcess/blob/master/Documentation/0002.jpg" />