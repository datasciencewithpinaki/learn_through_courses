#!/usr/bin/env python
from learn_multiagents.crew import LearnMultiagentsCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    LearnMultiagentsCrew().crew().kickoff(inputs=inputs)