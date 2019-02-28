import redis

r = redis.Redis(host='localhost', port=6379, password='xzx199110')
r.set('age', '199110')

r.hset('bin', 'name', 'xiao')
r.hset('bin', 'name', 'jian')
r.hset('usr', 'name', 'xiaojian')

print(r.hget('bin', 'name'))
print(r.hget('usr', 'name'))

