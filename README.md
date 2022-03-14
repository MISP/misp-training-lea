# misp-training-lea

Practical Information Sharing between Law Enforcement and CSIRT communities using MISP. The training is composed of theoritical and practical modules. A part of the practical modules include specific topics such as network forensic analysis, system forensic and threat analysis. The focus of the modules is show the complete chain from incident response, analysis up to the modeling and sharing with MISP.

## Modules

- [Isolate Threat Actor(s) from Network Captures - (e.304)](./e.304-isolate-threat-actor-from-network-capture)

## Further readings

- Neolea trainings

# Course codes

- `1xx` - Introductory
- `2xx` - Intermediate
- `3xx` - Advanced

# Compiling slides
Simply run the command below to compile the slides
```bash
./build.sh
```
The slides and their associated handouts can be found in `output`.

# Contributing

Review the [conventions](conventions.md) for the directory structure and required information, then you can make a pull-request to contribute a new training.

For existing content, a pull-request can be done.

To create a new slide deck:
1. copy the `blueprint` directory
2. rename it to match the course name: `e.xxx-my-course`
3. edit `e.xxx-my-course/slides.tex` to update the course title
4. edit `e.xxx-my-course/content.tex` to add the course's content
5. include `e.xxx-my-course` in the list of the slidecks variables in the build file `build.sh`
6. run `build.sh` to compile it

# License

All the materials are dual-licensed under GNU Affero General Public License version 3 or later and the Creative Commons Attribution-ShareAlike 4.0 International. You can use either one of the licenses depending of your use case of the training materials.

# Contributors in alphabetical order

- Alexandre Dulaunoy
- Andras Iklody
- Sami Mokaddem
