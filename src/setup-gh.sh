#! /usr/bin/env bash

# This script sets up the authentication parameters for the GitHub CLI
# that are needed to run the version2.py script.
# It is assumed that the GitHub CLI is already installed and configured
# on the system.
# The script will update the user's github token to have the needed scopes,
# set the token in the environment and pull in the gh users username as
# another environment variable.

# Exit if not sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "ERROR: This script must be sourced, not executed."
  echo "Usage: source ${BASH_SOURCE[0]}"
  exit 1
fi

# Check if the GITHUB_TOKEN environment variable is already set
set_gh_token() {
    # If not set, set the scopes for the token and set the enviornment variable
    gh auth refresh --scopes read:project

    # Set the GITHUB_TOKEN environment variable
    export GITHUB_TOKEN=$(gh auth token)
}


configure_gh_env() {
    if [ -n "${GITHUB_TOKEN}" ]; then
        echo "GITHUB_TOKEN needs to be unset to update the token scopes."
        unset GITHUB_TOKEN
    fi

    # set the gh_token
    set_gh_token

    # set the gh_user
    export GITHUB_UNAME=$(gh api user --jq .login)

    echo "GITHUB_TOKEN is set. Length is: ${#GITHUB_TOKEN}"
    echo "GITHUB_UNAME is set to: ${GITHUB_UNAME}"
}

configure_gh_env
