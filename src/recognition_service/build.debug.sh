#! /bin/bash
echo "Launching recognition service\n"
export ENV="debug"
uvicorn app:app