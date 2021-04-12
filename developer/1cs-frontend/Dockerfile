# base image
FROM node:12

# set working directory
RUN mkdir /app
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
ADD package.json package-lock.json /app/
RUN npm install

# Copy all frontend code to new "app" folder
COPY . /app/

EXPOSE 8000

CMD ["gatsby", "develop", "-H", "0.0.0.0"]

