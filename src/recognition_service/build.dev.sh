#! /bin/bash
echo "Launching recognition service\n"
export ENV="dev"
uvicorn app:app