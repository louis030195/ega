import os
import requests
import pandas as pd
import re
from flask import request, jsonify

ouraring_token = os.environ["OURARING_TOKEN"]


def ega_public(_):
    """something"""

    # Set CORS headers for the preflight request
    if request.method == "OPTIONS":
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": ["Content-Type", "X-Api-Key"],
            "Access-Control-Max-Age": "3600",
        }

        return (
            jsonify(
                {
                    "error": {
                        "message": "This is a preflight request.",
                        "status": "preflight",
                    },
                }
            ),
            204,
            headers,
        )

    # Set CORS headers for the main request
    headers = {"Access-Control-Allow-Origin": "*"}

    url = "https://api.ouraring.com/v2/usercollection/daily_readiness"
    params = {"start_date": "2021-11-01", "end_date": "2023-12-01"}
    headers = {"Authorization": "Bearer " + ouraring_token}

    daily_readiness_df = pd.json_normalize(
        requests.request("GET", url, headers=headers, params=params).json()["data"],
    )
    # replace all columns starting with "contributors." by "daily_readiness_"
    daily_readiness_df.columns = [
        re.sub(r"^contributors\.", "daily_readiness_", col)
        for col in daily_readiness_df.columns
    ]
    # replace "score" by "daily_readiness_score"
    daily_readiness_df.columns = [
        re.sub(r"^score$", "daily_readiness_score", col)
        for col in daily_readiness_df.columns
    ]

    return (
        jsonify(daily_readiness_df.to_dict(orient="records")[-1]),
        200,
        headers,
    )
