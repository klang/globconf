# Integration between GitHub and VisualStudio

https://docs.microsoft.com/en-us/vsts/pipelines/build/ci-build-github?view=vsts&tabs=yaml

## Status badge

Under "Build and release" for the project, select "options", copy the "Status badge" Markdown link to the Readme.md file of the project.

[![Build status](https://cloudpartners.visualstudio.com/MyFirstProject/_apis/build/status/MyFirstProject-Python%20package-CI)](https://cloudpartners.visualstudio.com/MyFirstProject/_build/latest?definitionId=2)

If the image is broken above, or [this](https://cloudpartners.visualstudio.com/MyFirstProject/_apis/build/status/MyFirstProject-Python%20package-CI) link returns the following error in an anonymous browser, then the TFTS Organisation need to allow public projects AND the project need to be public.

    {"$id":"1","innerException":null,"message":"TF50309: The following account does not have sufficient permissions to complete the operation: Anonymous. The following permissions are needed to perform this operation: View project-level information.","typeName":"System.UnauthorizedAccessException, mscorlib","typeKey":"UnauthorizedAccessException","errorCode":0,"eventId":0}

Turn on anonymous access to projects [here](https://cloudpartners.visualstudio.com/_admin/_policy)

Then, make the project public, under "specific people", [here](https://cloudpartners.visualstudio.com/MyFirstProject/_admin)

The relevant documentation for Microsoft VSTS is [here](https://docs.microsoft.com/en-us/vsts/organizations/public/make-project-public?view=vsts&tabs=previous-nav)

### PyPi server

    mkdir -p ~/projects/pypiserver/data
    cd ~/projects/pypiserver/
    
    htpasswd -sc ~/projects/pypiserver/data/.htaccess some_username
    
create a docker-compose.yml file with the following content:

    ---
    ########################################################################
    # pypiserver docker-compose example
    ########################################################################
    
    version: "3.3"
    
    services:
        pypiserver:
            image: pypiserver/pypiserver:latest
            volumes:
                - type: bind
                  source: ./data
                  target: /data
            # Use an .htaccess file to control access, serve packages from
            # ./data (which will be /data in the container)
            command: -P /data/.htaccess -a update,download,list /data/packages
            ports:
                - "80:8080"
    volumes:
        data:    
    
start up the container:

    (pypiserver) [klang@bascule pypiserver]$ docker-compose up
    Creating network "pypiserver_default" with the default driver
    Creating volume "pypiserver_data" with default driver
    Creating pypiserver_pypiserver_1 ... done
    Attaching to pypiserver_pypiserver_1
    
### Packing

    python setup.py sdist
    twine upload -u some_username -p abc123 --repository-url http://localhost dist/* --skip-existing

    twine upload --repository-url http://upload.pypi.org/legacy/ dist/*
    twine upload --repository-url http://test.pypi.org/legacy/ dist/*



    open https://pypi.org/project/klang-globconf/


### Test that package can be installed

    pyenv virtualenv 3.6.5 testing
    pyenv activate testing
    pip install --index-url http://some_username:abc123@localhost  globconf
    pip uninstall globconf
    pyenv deactivate
    pyenv uninstall -f testing


### Build

    brew install pyenv
    brew install pyenv-virtualenv
    brew install pyenv-virtualenvwrapper
    pyenv install 3.6.5
    pyenv virtualenv 3.6.5 globconf
    pyenv activate globconf
    
    pip install twine
    
    
