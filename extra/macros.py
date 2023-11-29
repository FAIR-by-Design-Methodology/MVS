import os

def define_env(env):
    "Hook function"

    @env.macro
    def glossary():
        terms = {}
        with open('definitions.md', 'r') as glossary:
            for line in glossary:
                 parts = str.split(line, ']:')
                 if len(parts) == 2:
                      parts[0] = str.strip(str.replace(parts[0], '*[', ''))
                      parts[1] = str.strip(parts[1])
                      terms[parts[0]] = parts[1]
        return terms