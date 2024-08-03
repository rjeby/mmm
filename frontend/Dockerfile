# Use the latest Node.js image from Docker Hub as the base image
FROM node:lts-alpine as build-stage

# Set the working directory inside the container
WORKDIR /frontend

# Copy package.json and package-lock.json (if available) to the working directory
COPY ./frontend/package*.json ./

# Install the project dependencies specified in package.json
RUN npm install

# Copy all files from the current directory on the host to the working directory in the container
COPY ./frontend/ .

# Build the project (assuming there's a build script defined in package.json)
RUN npm run build

# # Install the 'serve' package globally to serve the built project
# RUN npm install -g serve

# # Define the command to run the container, serving the build output using 'serve' in single-page application mode
# CMD ["serve", "-s", "dist"]

# Use the lightweight Nginx image from the previous stage for the nginx container
FROM nginx:stable-alpine as production-stage

# Copy the build application from the previous stage to the Nginx container
COPY --from=build-stage /frontend/dist /usr/share/nginx/html

# Copy the nginx configuration file
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
# Start Nginx to serve the application
CMD ["nginx", "-g", "daemon off;"]
