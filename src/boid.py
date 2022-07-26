from vector import Vector
import numpy
import math
import random


class Boid:

    def __init__(self, width, height):

 
        self.width = width
        self.height = height
        self.position = Vector(random.randint(0, width), random.randint(0, height))
        self.velocity = Vector(random.uniform(-2,2),random.uniform(-2,2))
        self.velocity.set_mag(random.randint(1,10))
        self.acceleration = Vector(0,0)
        self.perception = 75
        self.max_force = 0.8
        self.sep_force = 0
        self.coh_force = 0
        self.align_force = 1
        self.max_speed = 5

    def update(self):

        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
        self.velocity.limit_mag(self.max_speed)
        self.acceleration = Vector(0,0)
    
    def edges(self):

        if self.position.x > self.width:
            self.position.x = 0
        elif self.position.x < 0: 
            self.position.x = self.width
        if self.position.y > self.height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.height

    
    def align(self, boids):

        steering  = Vector(0,0)
        total = 0
        for boid in boids:
            if self != boid and self.position.dist(boid.position) < self.perception:
                steering.add(boid.velocity)
                total += 1
        if total > 0:
            steering.div(total)
            steering.set_mag(self.max_speed)
            steering.sub(self.velocity)
            steering.limit_mag(self.max_force)

        return steering

    def cohesion(self, boids):

        steering = Vector(0,0)
        total = 0
        for boid in boids:
            if self != boid and self.position.dist(boid.position) < self.perception:
                steering.add(boid.position)
                total += 1
        if total > 0:
            steering.div(total)
            steering.sub(self.position)
            steering.set_mag(self.max_speed)
            steering.sub(self.velocity)
            steering.limit_mag(self.max_force)

        return steering

    def separation(self, boids):

        steering = Vector(0,0)
        total = 0
        for boid in boids:
            dist = self.position.dist(boid.position)
            if self != boid and dist < self.perception:
                difference = Vector(self.position.x - boid.position.x, self.position.y - boid.position.y)
                if(dist > 0):
                    difference.div(dist * dist)
                steering.add(difference)
                total += 1
        if total > 0:
            steering.div(total)
            steering.set_mag(self.max_speed)
            steering.sub(self.velocity)
            steering.limit_mag(self.max_force)

        return steering

    def flock(self, boids):

        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        seperation = self.separation(boids)
        alignment.scale(self.align_force)
        cohesion.scale(self.coh_force)
        seperation.scale(self.sep_force)
        self.acceleration.add(seperation)
        self.acceleration.add(alignment)
        self.acceleration.add(cohesion)