# chmod +x dlo.sh
if [ $1 == 'start' ]
    then
        docker-compose up
fi
if [ $1 == 'stop' ]
    then
        docker-compose down
fi
if [ $1 == 'restart' ]
    then
        docker-compose down
        docker-compose up
fi
if [ $1 == 'build' ]
    then
        docker-compose build
fi
if [ $1 == 'backgroud_start' ]
    then
        docker-compose up -d
fi
if [ $1 == 'rebuild' ]
    then
        docker-compose up --build
fi
if [ $1 == 'h_rebuild' ]
    then
        docker-compose build
        docker-compose up
fi
