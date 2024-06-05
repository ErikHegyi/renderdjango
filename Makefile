build:
    docker build --force-rm $(options) -t VAGKereso:latest .

build-prod:
    $(MAKE) build options="--target production"
