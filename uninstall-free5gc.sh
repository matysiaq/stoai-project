#!/bin/bash

# Fetch the list of Helm charts
helm_list=$(helm list -q)

# Iterate over each chart in the list
for chart in $helm_list; do
    # Check if the chart name matches 'free5gc-*'
    if [[ $chart == free5gc-* ]]; then
        echo "Deleting Helm chart: $chart"
        # Delete the matching Helm chart
        helm uninstall $chart
    fi
done

echo "All matching Helm charts have been removed."
