# ega

⚠️ Highly experimental ⚠️

Ego but female, because all AI assistants are female.

The goal is to implement tools that

1. Collect data about your inputs
2. Collect data about your outputs
3. Provide tools to run life experiments and interpret

See [issues](https://github.com/louis030195/ega/issues) for discussing ideas.

## Desired API

```py
import ega

# call wandb, create ouraring tags, time entries in timingapp, etc.
ega.start_experiment(name="vegan_keto_diet")

# a week later
ega.stop_experiment(name="vegan_keto_diet")

# or

name = "polyphasic_sleep"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "no_alcohol"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "no_phone"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "carnivorous"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "insectivorous"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "resistance_training_0.2.4"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "social_orgy"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "social_fasting"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "ashwagandha"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "creatine"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)

# or

name = "nootropics_party"

ega.start_experiment(name=name)

# a week later
ega.stop_experiment(name=name)
```

## Why?

- Collecting & joining private data as a product is not culturally acceptable


