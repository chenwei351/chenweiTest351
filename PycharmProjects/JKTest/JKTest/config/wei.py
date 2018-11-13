# -*- utf-8 -*-
import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

add = a + b
add_and_triple = add * 3.
print(a)
print(b)
print(add)
sess = tf.Session()
print(sess.run(add, {a: 3, b: 4.5}))
print(sess.run(add, {a: [1, 3], b: [2, 4]}))
print(sess.run(add_and_triple, {a: 3, b: 4.5}))