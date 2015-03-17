 // Include the flickr signing library
 y.include("http:blog.pipes.yahoo.net/wp-content/uploads/flickr.js");
 // GET the flickr result using a signed url
 var fs = new flickrSigner(api_key,secret);
 response.object = y.rest(fs.createUrl({method:method, format:""})).get().response();
