import pickle


LB = ['B-B','B-S','F-D','F-S','M-D','M-S','S-S']

for i, item in enumerate(LB):
    print(item)
    pth = '../data/label/{}.pkl'.format(item)
    with open(pth, 'rb') as fp:
        nemo_ls = pickle.load(fp)

    print(nemo_ls)



# B-B
B_B= [[1, 1, 'f02-1', 'f02-2'],
 [1, 1, 'f08-1', 'f08-3'],
 [1, 1, 'f10-1', 'f10-2'],
 [1, 0, 'f02-1', 'f08-3'],
 [1, 0, 'f08-1', 'f10-2'],
 [1, 0, 'f10-1', 'f02-2'],
 [2, 1, 'f28-2', 'f28-3'],
 [2, 1, 'f28-1', 'f28-2'],
 [2, 1, 'f28-1', 'f28-3'],
 [2, 0, 'f28-2', 'f05-1'],
 [2, 0, 'f28-1', 'f05-1'],
 [2, 0, 'f28-1', 'f05-1'],
 [3, 1, 'f22-1', 'f22-2'],
 [3, 1, 'f40-1', 'f40-3'],
 [3, 1, 'f42-2', 'f42-3'],
 [3, 0, 'f22-1', 'f40-3'],
 [3, 0, 'f40-1', 'f42-3'],
 [3, 0, 'f42-2', 'f22-2'],
 [4, 1, 'f52-1', 'f52-2'],
 [4, 1, 'f58-1', 'f58-4'],
 [4, 1, 'f66-2', 'f66-3'],
 [4, 0, 'f52-1', 'f58-4'],
 [4, 0, 'f58-1', 'f66-3'],
 [4, 0, 'f66-2', 'f52-2'],
 [5, 1, 'f78-3', 'f78-4'],
 [5, 1, 'f79-3', 'f79-4'],
 [5, 1, 'f84-2', 'f84-3'],
 [5, 0, 'f78-3', 'f84-3'],
 [5, 0, 'f79-3', 'f78-4'],
 [5, 0, 'f84-2', 'f79-4']]
# B-S
B_S= [[1, 1, 'f05-1', 'f05-2'],
 [1, 1, 'f09-4', 'f09-1'],
 [1, 1, 'f07-1', 'f07-4'],
 [1, 1, 'f19-1', 'f19-3'],
 [1, 1, 'f21-2', 'f21-3'],
 [1, 1, 'f25-1', 'f25-2'],
 [1, 0, 'f05-1', 'f25-2'],
 [1, 0, 'f09-4', 'f19-3'],
 [1, 0, 'f07-1', 'f09-1'],
 [1, 0, 'f19-1', 'f05-2'],
 [1, 0, 'f21-2', 'f07-4'],
 [1, 0, 'f25-1', 'f21-3'],
 [2, 1, 'f42-3', 'f42-1'],
 [2, 1, 'f30-2', 'f30-1'],
 [2, 1, 'f33-2', 'f33-1'],
 [2, 1, 'f36-1', 'f36-2'],
 [2, 1, 'f41-3', 'f41-4'],
 [2, 1, 'f42-2', 'f42-1'],
 [2, 0, 'f42-3', 'f30-1'],
 [2, 0, 'f30-2', 'f42-1'],
 [2, 0, 'f33-2', 'f42-1'],
 [2, 0, 'f36-1', 'f41-4'],
 [2, 0, 'f41-3', 'f33-1'],
 [2, 0, 'f42-2', 'f36-2'],
 [3, 1, 'f29-1', 'f29-2'],
 [3, 1, 'f43-1', 'f43-2'],
 [3, 1, 'f45-3', 'f45-4'],
 [3, 1, 'f49-3', 'f49-2'],
 [3, 1, 'f51-1', 'f51-3'],
 [3, 1, 'f51-2', 'f51-4'],
 [3, 0, 'f29-1', 'f51-4'],
 [3, 0, 'f43-1', 'f29-2'],
 [3, 0, 'f45-3', 'f49-2'],
 [3, 0, 'f49-3', 'f51-3'],
 [3, 0, 'f51-1', 'f43-2'],
 [3, 0, 'f51-2', 'f45-4'],
 [4, 1, 'f53-2', 'f53-3'],
 [4, 1, 'f61-2', 'f61-4'],
 [4, 1, 'f64-3', 'f64-2'],
 [4, 1, 'f68-1', 'f68-2'],
 [4, 1, 'f69-2', 'f69-1'],
 [4, 1, 'f72-1', 'f72-2'],
 [4, 0, 'f53-2', 'f72-2'],
 [4, 0, 'f61-2', 'f69-1'],
 [4, 0, 'f64-3', 'f61-4'],
 [4, 0, 'f68-1', 'f64-2'],
 [4, 0, 'f69-2', 'f53-3'],
 [4, 0, 'f72-1', 'f68-2'],
 [5, 1, 'f74-5', 'f74-1'],
 [5, 1, 'f74-5', 'f74-2'],
 [5, 1, 'f80-2', 'f80-1'],
 [5, 1, 'f81-1', 'f81-2'],
 [5, 1, 'f84-2', 'f84-1'],
 [5, 1, 'f84-3', 'f84-1'],
 [5, 0, 'f74-5', 'f80-1'],
 [5, 0, 'f74-5', 'f84-1'],
 [5, 0, 'f80-2', 'f74-1'],
 [5, 0, 'f81-1', 'f84-1'],
 [5, 0, 'f84-2', 'f81-2'],
 [5, 0, 'f84-3', 'f74-2']]
# F-D
F_D = [[1, 1, 'f03-3', 'f03-1'],
 [1, 1, 'f04-2', 'f04-1'],
 [1, 1, 'f05-3', 'f05-2'],
 [1, 1, 'f06-2', 'f06-1'],
 [1, 1, 'f19-2', 'f19-3'],
 [1, 1, 'f21-1', 'f21-3'],
 [1, 0, 'f03-3', 'f05-2'],
 [1, 0, 'f04-2', 'f21-3'],
 [1, 0, 'f05-3', 'f19-3'],
 [1, 0, 'f06-2', 'f03-1'],
 [1, 0, 'f19-2', 'f06-1'],
 [1, 0, 'f21-1', 'f04-1'],
 [2, 1, 'f27-1', 'f27-2'],
 [2, 1, 'f31-1', 'f31-2'],
 [2, 1, 'f31-1', 'f31-3'],
 [2, 1, 'f34-1', 'f34-2'],
 [2, 1, 'f36-3', 'f36-2'],
 [2, 1, 'f41-2', 'f41-4'],
 [2, 0, 'f27-1', 'f36-2'],
 [2, 0, 'f31-1', 'f34-2'],
 [2, 0, 'f31-1', 'f27-2'],
 [2, 0, 'f34-1', 'f41-4'],
 [2, 0, 'f36-3', 'f31-3'],
 [2, 0, 'f41-2', 'f31-2'],
 [3, 1, 'f42-5', 'f42-1'],
 [3, 1, 'f45-5', 'f45-4'],
 [3, 1, 'f46-4', 'f46-2'],
 [3, 1, 'f46-4', 'f46-3'],
 [3, 1, 'f49-1', 'f49-2'],
 [3, 1, 'f53-1', 'f53-3'],
 [3, 0, 'f42-5', 'f46-3'],
 [3, 0, 'f45-5', 'f53-3'],
 [3, 0, 'f46-4', 'f49-2'],
 [3, 0, 'f46-4', 'f42-1'],
 [3, 0, 'f49-1', 'f46-2'],
 [3, 0, 'f53-1', 'f45-4'],
 [4, 1, 'f74-3', 'f74-2'],
 [4, 1, 'f58-3', 'f58-2'],
 [4, 1, 'f59-2', 'f59-1'],
 [4, 1, 'f60-1', 'f60-2'],
 [4, 1, 'f64-1', 'f64-2'],
 [4, 1, 'f74-3', 'f74-1'],
 [4, 0, 'f74-3', 'f59-1'],
 [4, 0, 'f58-3', 'f74-2'],
 [4, 0, 'f59-2', 'f64-2'],
 [4, 0, 'f60-1', 'f74-1'],
 [4, 0, 'f64-1', 'f60-2'],
 [4, 0, 'f74-3', 'f58-2'],
 [5, 1, 'f55-1', 'f55-2'],
 [5, 1, 'f83-3', 'f83-1'],
 [5, 1, 'f83-3', 'f83-2'],
 [5, 1, 'f84-4', 'f84-1'],
 [5, 1, 'f85-1', 'f85-2'],
 [5, 1, 'f85-1', 'f85-3'],
 [5, 0, 'f55-1', 'f85-3'],
 [5, 0, 'f83-3', 'f85-2'],
 [5, 0, 'f83-3', 'f84-1'],
 [5, 0, 'f84-4', 'f83-1'],
 [5, 0, 'f85-1', 'f55-2'],
 [5, 0, 'f85-1', 'f83-2']]
# F-S
F_S = [[1, 1, 'f05-3', 'f05-1'],
 [1, 1, 'f07-2', 'f07-3'],
 [1, 1, 'f10-3', 'f10-2'],
 [1, 1, 'f10-3', 'f10-1'],
 [1, 1, 'f11-2', 'f11-1'],
 [1, 1, 'f17-3', 'f17-2'],
 [1, 0, 'f05-3', 'f11-1'],
 [1, 0, 'f07-2', 'f05-1'],
 [1, 0, 'f10-3', 'f07-3'],
 [1, 0, 'f10-3', 'f17-2'],
 [1, 0, 'f11-2', 'f10-2'],
 [1, 0, 'f17-3', 'f10-1'],
 [2, 1, 'f19-2', 'f19-1'],
 [2, 1, 'f21-1', 'f21-2'],
 [2, 1, 'f22-3', 'f22-1'],
 [2, 1, 'f22-3', 'f14-2'],
 [2, 1, 'f36-3', 'f36-1'],
 [2, 1, 'f38-2', 'f38-1'],
 [2, 0, 'f19-2', 'f38-1'],
 [2, 0, 'f21-1', 'f22-1'],
 [2, 0, 'f22-3', 'f21-2'],
 [2, 0, 'f22-3', 'f36-1'],
 [2, 0, 'f36-3', 'f19-1'],
 [2, 0, 'f38-2', 'f14-2'],
 [3, 1, 'f40-4', 'f40-1'],
 [3, 1, 'f40-4', 'f40-3'],
 [3, 1, 'f41-2', 'f41-3'],
 [3, 1, 'f42-5', 'f42-2'],
 [3, 1, 'f42-5', 'f42-3'],
 [3, 1, 'f45-5', 'f45-3'],
 [3, 0, 'f40-4', 'f42-2'],
 [3, 0, 'f40-4', 'f42-3'],
 [3, 0, 'f41-2', 'f45-3'],
 [3, 0, 'f42-5', 'f41-3'],
 [3, 0, 'f42-5', 'f40-3'],
 [3, 0, 'f45-5', 'f40-1'],
 [4, 1, 'f47-3', 'f47-4'],
 [4, 1, 'f49-1', 'f49-3'],
 [4, 1, 'f52-3', 'f52-1'],
 [4, 1, 'f52-3', 'f52-2'],
 [4, 1, 'f53-1', 'f53-2'],
 [4, 1, 'f56-2', 'f56-3'],
 [4, 0, 'f47-3', 'f52-2'],
 [4, 0, 'f49-1', 'f52-1'],
 [4, 0, 'f52-3', 'f47-4'],
 [4, 0, 'f52-3', 'f56-3'],
 [4, 0, 'f53-1', 'f49-3'],
 [4, 0, 'f56-2', 'f53-2'],
 [5, 1, 'f57-1', 'f57-2'],
 [5, 1, 'f58-5', 'f58-1'],
 [5, 1, 'f58-5', 'f58-4'],
 [5, 1, 'f61-2', 'f61-1'],
 [5, 1, 'f64-1', 'f64-3'],
 [5, 1, 'f74-3', 'f74-5'],
 [5, 1, 'f78-2', 'f78-3'],
 [5, 1, 'f78-2', 'f78-4'],
 [5, 1, 'f84-4', 'f84-2'],
 [5, 1, 'f84-4', 'f84-3'],
 [5, 0, 'f57-1', 'f58-4'],
 [5, 0, 'f58-5', 'f84-3'],
 [5, 0, 'f58-5', 'f78-4'],
 [5, 0, 'f61-2', 'f84-2'],
 [5, 0, 'f64-1', 'f58-1'],
 [5, 0, 'f74-3', 'f78-3'],
 [5, 0, 'f78-2', 'f57-2'],
 [5, 0, 'f78-2', 'f64-3'],
 [5, 0, 'f84-4', 'f61-1'],
 [5, 0, 'f84-4', 'f74-5']]
# M-D
M_D= [[1, 1, 'f03-1', 'f03-2'],
 [1, 1, 'f09-2', 'f09-1'],
 [1, 1, 'f13-2', 'f13-1'],
 [1, 1, 'f14-2', 'f14-1'],
 [1, 1, 'f18-1', 'f18-2'],
 [1, 1, 'f18-1', 'f18-3'],
 [1, 1, 'f19-4', 'f19-3'],
 [1, 1, 'f20-2', 'f20-1'],
 [1, 1, 'f21-4', 'f21-3'],
 [1, 0, 'f03-1', 'f14-1'],
 [1, 0, 'f09-2', 'f20-1'],
 [1, 0, 'f13-2', 'f21-3'],
 [1, 0, 'f14-2', 'f18-2'],
 [1, 0, 'f18-1', 'f19-3'],
 [1, 0, 'f18-1', 'f03-2'],
 [1, 0, 'f19-4', 'f13-1'],
 [1, 0, 'f20-2', 'f09-1'],
 [1, 0, 'f21-4', 'f18-3'],
 [2, 1, 'f24-1', 'f24-2'],
 [2, 1, 'f26-2', 'f26-1'],
 [2, 1, 'f27-3', 'f27-2'],
 [2, 1, 'f29-3', 'f29-2'],
 [2, 1, 'f30-3', 'f30-1'],
 [2, 1, 'f32-1', 'f32-2'],
 [2, 1, 'f33-3', 'f33-1'],
 [2, 1, 'f37-2', 'f37-1'],
 [2, 1, 'f39-2', 'f39-1'],
 [2, 0, 'f24-1', 'f30-1'],
 [2, 0, 'f26-2', 'f24-2'],
 [2, 0, 'f27-3', 'f26-1'],
 [2, 0, 'f29-3', 'f37-1'],
 [2, 0, 'f30-3', 'f39-1'],
 [2, 0, 'f32-1', 'f33-1'],
 [2, 0, 'f33-3', 'f32-2'],
 [2, 0, 'f37-2', 'f27-2'],
 [2, 0, 'f39-2', 'f29-2'],
 [3, 1, 'f41-1', 'f41-4'],
 [3, 1, 'f42-4', 'f42-1'],
 [3, 1, 'f43-5', 'f43-2'],
 [3, 1, 'f43-4', 'f43-3'],
 [3, 1, 'f44-3', 'f44-1'],
 [3, 1, 'f44-3', 'f44-2'],
 [3, 1, 'f45-2', 'f45-4'],
 [3, 1, 'f46-1', 'f46-2'],
 [3, 1, 'f46-1', 'f46-3'],
 [3, 0, 'f41-1', 'f44-2'],
 [3, 0, 'f42-4', 'f46-2'],
 [3, 0, 'f43-5', 'f45-4'],
 [3, 0, 'f43-4', 'f44-1'],
 [3, 0, 'f44-3', 'f43-2'],
 [3, 0, 'f44-3', 'f41-4'],
 [3, 0, 'f45-2', 'f46-3'],
 [3, 0, 'f46-1', 'f43-3'],
 [3, 0, 'f46-1', 'f42-1'],
 [4, 1, 'f47-1', 'f47-2'],
 [4, 1, 'f50-3', 'f50-1'],
 [4, 1, 'f50-3', 'f50-2'],
 [4, 1, 'f51-5', 'f51-3'],
 [4, 1, 'f53-4', 'f53-3'],
 [4, 1, 'f63-2', 'f63-1'],
 [4, 1, 'f64-4', 'f64-2'],
 [4, 1, 'f65-3', 'f65-2'],
 [4, 1, 'f65-4', 'f65-3'],
 [4, 0, 'f47-1', 'f50-2'],
 [4, 0, 'f50-3', 'f63-1'],
 [4, 0, 'f50-3', 'f64-2'],
 [4, 0, 'f51-5', 'f65-3'],
 [4, 0, 'f53-4', 'f51-3'],
 [4, 0, 'f63-2', 'f47-2'],
 [4, 0, 'f64-4', 'f65-2'],
 [4, 0, 'f65-3', 'f53-3'],
 [4, 0, 'f65-4', 'f50-1'],
 [5, 1, 'f68-3', 'f68-2'],
 [5, 1, 'f69-3', 'f69-1'],
 [5, 1, 'f70-1', 'f70-2'],
 [5, 1, 'f73-1', 'f73-2'],
 [5, 1, 'f73-1', 'f73-3'],
 [5, 1, 'f74-4', 'f74-1'],
 [5, 1, 'f74-4', 'f74-2'],
 [5, 1, 'f77-1', 'f77-2'],
 [5, 1, 'f77-1', 'f77-3'],
 [5, 1, 'f80-3', 'f80-1'],
 [5, 0, 'f68-3', 'f73-2'],
 [5, 0, 'f69-3', 'f77-2'],
 [5, 0, 'f70-1', 'f69-1'],
 [5, 0, 'f73-1', 'f74-2'],
 [5, 0, 'f73-1', 'f68-2'],
 [5, 0, 'f74-4', 'f70-2'],
 [5, 0, 'f74-4', 'f77-3'],
 [5, 0, 'f77-1', 'f73-3'],
 [5, 0, 'f77-1', 'f80-1'],
 [5, 0, 'f80-3', 'f74-1']]
# M-S
M_S = [[1, 1, 'f22-4', 'f22-2'],
 [1, 1, 'f07-4', 'f07-3'],
 [1, 1, 'f09-2', 'f09-4'],
 [1, 1, 'f12-1', 'f12-2'],
 [1, 1, 'f17-1', 'f17-2'],
 [1, 1, 'f19-4', 'f19-1'],
 [1, 1, 'f21-4', 'f21-2'],
 [1, 1, 'f22-4', 'f22-1'],
 [1, 0, 'f22-4', 'f09-4'],
 [1, 0, 'f07-4', 'f17-2'],
 [1, 0, 'f09-2', 'f12-2'],
 [1, 0, 'f12-1', 'f19-1'],
 [1, 0, 'f17-1', 'f21-2'],
 [1, 0, 'f19-4', 'f22-2'],
 [1, 0, 'f21-4', 'f22-1'],
 [1, 0, 'f22-4', 'f07-3'],
 [2, 1, 'f40-2', 'f40-3'],
 [2, 1, 'f29-3', 'f29-1'],
 [2, 1, 'f30-3', 'f30-2'],
 [2, 1, 'f33-3', 'f33-2'],
 [2, 1, 'f35-2', 'f35-1'],
 [2, 1, 'f35-2', 'f35-3'],
 [2, 1, 'f38-3', 'f38-1'],
 [2, 1, 'f40-2', 'f40-1'],
 [2, 0, 'f40-2', 'f38-1'],
 [2, 0, 'f29-3', 'f40-3'],
 [2, 0, 'f30-3', 'f35-1'],
 [2, 0, 'f33-3', 'f35-3'],
 [2, 0, 'f35-2', 'f29-1'],
 [2, 0, 'f35-2', 'f30-2'],
 [2, 0, 'f38-3', 'f40-1'],
 [2, 0, 'f40-2', 'f33-2'],
 [3, 1, 'f01-1', 'f01-2'],
 [3, 1, 'f41-1', 'f41-3'],
 [3, 1, 'f42-4', 'f42-2'],
 [3, 1, 'f42-4', 'f42-3'],
 [3, 1, 'f43-5', 'f43-1'],
 [3, 1, 'f45-2', 'f45-3'],
 [3, 1, 'f48-3', 'f48-2'],
 [3, 1, 'f51-5', 'f51-1'],
 [3, 0, 'f01-1', 'f42-2'],
 [3, 0, 'f41-1', 'f45-3'],
 [3, 0, 'f42-4', 'f01-2'],
 [3, 0, 'f42-4', 'f48-2'],
 [3, 0, 'f43-5', 'f51-1'],
 [3, 0, 'f45-2', 'f42-3'],
 [3, 0, 'f48-3', 'f41-3'],
 [3, 0, 'f51-5', 'f43-1'],
 [4, 1, 'f66-1', 'f66-3'],
 [4, 1, 'f56-1', 'f56-3'],
 [4, 1, 'f58-2', 'f58-1'],
 [4, 1, 'f58-2', 'f58-4'],
 [4, 1, 'f61-4', 'f61-3'],
 [4, 1, 'f62-2', 'f62-1'],
 [4, 1, 'f64-4', 'f64-3'],
 [4, 1, 'f66-1', 'f66-2'],
 [4, 0, 'f66-1', 'f64-3'],
 [4, 0, 'f56-1', 'f66-3'],
 [4, 0, 'f58-2', 'f61-3'],
 [4, 0, 'f58-2', 'f62-1'],
 [4, 0, 'f61-4', 'f58-1'],
 [4, 0, 'f62-2', 'f58-4'],
 [4, 0, 'f64-4', 'f66-2'],
 [4, 0, 'f66-1', 'f56-3'],
 [5, 1, 'f53-4', 'f53-2'],
 [5, 1, 'f67-2', 'f67-1'],
 [5, 1, 'f68-3', 'f68-1'],
 [5, 1, 'f69-3', 'f69-2'],
 [5, 1, 'f74-4', 'f74-5'],
 [5, 1, 'f75-2', 'f75-1'],
 [5, 1, 'f78-1', 'f78-3'],
 [5, 1, 'f78-1', 'f78-4'],
 [5, 1, 'f80-3', 'f80-2'],
 [5, 0, 'f53-4', 'f78-4'],
 [5, 0, 'f67-2', 'f80-2'],
 [5, 0, 'f68-3', 'f74-5'],
 [5, 0, 'f69-3', 'f78-3'],
 [5, 0, 'f74-4', 'f67-1'],
 [5, 0, 'f75-2', 'f68-1'],
 [5, 0, 'f78-1', 'f69-2'],
 [5, 0, 'f78-1', 'f75-1'],
 [5, 0, 'f80-3', 'f53-2']]
# S-S

S_S = [[1, 1, 'f18-2', 'f18-3'],
 [1, 1, 'f31-2', 'f31-3'],
 [1, 1, 'f43-4', 'f43-5'],
 [1, 0, 'f18-2', 'f43-5'],
 [1, 0, 'f31-2', 'f18-3'],
 [1, 0, 'f43-4', 'f31-3'],
 [2, 1, 'f44-1', 'f44-2'],
 [2, 1, 'f46-2', 'f46-3'],
 [2, 1, 'f50-1', 'f50-2'],
 [2, 0, 'f44-1', 'f50-2'],
 [2, 0, 'f46-2', 'f44-2'],
 [2, 0, 'f50-1', 'f46-3'],
 [3, 1, 'f65-1', 'f65-5'],
 [3, 1, 'f71-1', 'f71-2'],
 [3, 1, 'f73-2', 'f73-3'],
 [3, 0, 'f65-1', 'f73-3'],
 [3, 0, 'f71-1', 'f65-5'],
 [3, 0, 'f73-2', 'f71-2'],
 [4, 1, 'f74-1', 'f74-2'],
 [4, 1, 'f76-1', 'f76-2'],
 [4, 1, 'f77-2', 'f77-3'],
 [4, 0, 'f74-1', 'f76-2'],
 [4, 0, 'f76-1', 'f77-3'],
 [4, 0, 'f77-2', 'f74-2'],
 [5, 1, 'f82-1', 'f82-2'],
 [5, 1, 'f83-1', 'f83-2'],
 [5, 1, 'f85-2', 'f85-3'],
 [5, 0, 'f82-1', 'f83-2'],
 [5, 0, 'f83-1', 'f85-3'],
 [5, 0, 'f85-2', 'f82-2']]


