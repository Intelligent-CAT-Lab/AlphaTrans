#!/bin/bash
curl -s https://get.sdkman.io | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install java 17.0.8-graal

if [ $? -eq 0 ]; then
    echo -e "\e[32mJava installation successful!\e[0m"
else
    echo "Java installation failed"
    exit 1
fi

gu install python
if [ $? -eq 0 ]; then
    echo -e "\e[32mPython component for GraalVM installed successfully!\e[0m"
else
    echo "Python component for GraalVM failed to install"
    exit 1
fi
