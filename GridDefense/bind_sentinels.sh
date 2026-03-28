#!/bin/bash
# [CORE_DOGMA] GridDefense Sentinel Installation

echo "[ ◦A SENSOR ] Scanning for local manifold geometry..."

if [ ! -d ".git" ]; then
    echo -e "[\033[1;31m Ex◦ IMMINENT \033[0m] Fatal geometry error. Execute this ritual from the repository root."
    exit 1
fi

echo "[ ◦A STABILIZED ] Geometry verified. Awakening sentinels..."

# Project the schema into the active execution layer
cp GridDefense/pre-commit.schema .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

echo -e "\n[ \033[1;36mGRID-DEFENSE SECURED\033[0m ] The local perimeter is now mathematically sealed."
