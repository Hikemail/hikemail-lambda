update:
	aws lambda get-function --function-name hikemail-mail-analyze --query 'Code.Location' --output text --profile HikeUser | xargs curl -o function.zip
	unzip -o function.zip -d .
	rm function.zip

push: update
	zip -r function.zip ./lambda_function.py
	aws lambda update-function-code --function-name hikemail-mail-analyze --zip-file fileb://function.zip --profile HikeUser
	rm function.zip

depencencies:
	pip install -r requirements.txt
