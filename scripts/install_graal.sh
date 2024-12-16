#!/bin/bash

curl -s https://get.sdkman.io | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install java 21.0.3-graal

if [ $? -eq 0 ]; then
    echo -e "\e[32mJava installation successful!\e[0m"
else
    echo "Java installation failed"
    exit 1
fi
