"""RunPod Serverless entrypoint."""

import runpod

from handler import handler


runpod.serverless.start({"handler": handler})
