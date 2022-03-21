# misp-training-lea - Practical Information Sharing between Law Enforcement and CSIRT communities using MISP

Practical Information Sharing between Law Enforcement and CSIRT communities using MISP. The training is composed of theoritical and practical modules. A part of the practical modules include specific topics such as network forensic analysis, system forensic and threat analysis. The focus of the modules is show the complete chain from incident response, analysis up to the modeling and sharing with MISP.

## eLearning

This eLearning module is a prerequisite or refreshing module to read before the actual training sessions. This helps to ensure that all participants are inline with the basic knowledge of MISP. In the training modules, the various elements mentioned in this introduction will be completed in details (e.101-104, e.205-e.206 and e.302-e.304).

- [MISP: Introduction, Concepts and Guide - PDF](https://github.com/MISP/misp-training-lea/raw/main/output/0_eLearning.pdf)

## Modules

- [Extract an Executable from PCAP & Investigating an Attack on a Linux Host (e.303)](./e.303-lab2-encoding-information-and-sharing-it)
- [Isolate Threat Actor(s) from Network Captures - (e.304)](./e.304-lab3-encoding-information-and-sharing-it-2)

## Infrastructure required

At minimum, a dedicated MISP instance is available for the students and trainers. A network of MISP instances can be also set up in order to conduct additional sharing exercises between the teams.

Each individual participant would connect to the MISP instance(s) from their workstations / laptops, where the requirement would simply be network access (TCP port 80/443 towards the MISP instances) and an Internat browser.

Additionally, students will need to have wireshark installed or at the very least have system permissions to download and run wireshark as well as deploy custom extensions for it.

## Further readings

- [Neolea trainings](https://github.com/neolea/neolea-training-materials)

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
