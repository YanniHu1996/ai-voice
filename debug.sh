cat ./.github/workflows/transform.yml |
    yq '.jobs.transform.steps[] | select(.id == "check-task") | .run' |
    sh
