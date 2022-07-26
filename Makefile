

install:
	@pip3 install --default-timeout=900 -r requirements.txt

clean:
	@rm -rf src/__pycache__
