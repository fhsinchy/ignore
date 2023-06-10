# ignore

Like the name suggests, this Python script is capable of generating a `.gitignore` file against a given template name.

## Requirements

* Python 3

## Installation

```shell
pip install git+https://github.com/fhsinchy/ignore.git#egg=ignore
pip freeze
```

Output &ndash;

```shell
ignore==1.0.0
```

## Usage

Once you have installed the package it should be available everywhere in your system. The generic command for executing this script is

```shell
ignore <name of the template>
```

If the given template name exists inside the [https://github.com/github/gitignore](https://github.com/github/gitignore) repository, the script will create a new `.gitignore` file in your current working directory.

You can get a list of all the available templates by executing the following command:

```shell
ignore templates
```

Be aware of the fact that the script will delete any pre-existing `.gitignore` file in the working directory bfore creating a new one. So if you have some custom addition to your existing file, copying that to your clipboard will be good idea.