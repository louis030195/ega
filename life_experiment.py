import fire
import wandb
import timingapp
import ouraring
import pandas as pd
import re
import requests

tokens = open(".env", "r").read()

def start_experiment(name: str, description: str):
    pass

def stop_experiment(name: str, description: str):
    pass


if __name__ == "__main__":
    fire.Fire({"start": start_experiment, "stop": stop_experiment})
