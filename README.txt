################################################
# Simple TOken Authentication with a Django API#
################################################

I will implement a simple Token Authentication with a Django API, simple cause this is not optimal, but still be used in some system today. This simple Token has to be understood before moving to advanced one. 

Enjoy 😎


#########
#Context#
#########

* I will create two model here: two models for two app:
    - The User model, which will be an extension of the AbstractUser with some additionnal fields
    
    - A post model.
we are building a fictive blog Api for posting, and retrieving data.

* I will set endpoint to subscribe/register , to login/authenticate, and parameterise permission to access data from the API upon authentication.

