FROM ubuntu:22.04

RUN   apt-get update -y
RUN   apt-get install -y apache2
RUN   echo "<h1>Hello, ECS ECR Docker Container Lab</h1>" > /var/www/html/index.html

#Configure apache web server
RUN   a2enmod rewrite
RUN   chown -R www-data:www-data /var/www
ENV   APACHE_RUN_USER www-data
ENV   APACHE_RUN_GROUP  www-data
ENV   APACHE_LOG_DIR  /var/log/apache2

EXPOSE   80
CMD   ["/usr/sbin/apache2ctl", "-DFOREGROUND"]