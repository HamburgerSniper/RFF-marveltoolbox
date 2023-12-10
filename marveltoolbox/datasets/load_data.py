from .cifar import load_cifar10
from .fashion_mnist import load_fmnist
from .mnist import load_mnist
from .svhn import load_svhn


def load_data(dataset, all_frac, train_frac, batch_size, img_size, label_list, is_norm=False, data_root='./DATASET'):
    if dataset == 'mnist':
        return load_mnist(data_root, all_frac, train_frac, batch_size, img_size=img_size, label_list=label_list,
                          is_norm=is_norm)
    elif dataset == 'svhn':
        return load_svhn(data_root, all_frac, train_frac, batch_size, img_size=img_size, label_list=label_list,
                         is_norm=is_norm)
    elif dataset == 'fmnist':
        return load_fmnist(data_root, all_frac, train_frac, batch_size, img_size=img_size, label_list=label_list,
                           is_norm=is_norm)
    elif dataset == 'cifar10':
        return load_cifar10(data_root, all_frac, train_frac, batch_size, img_size=img_size, label_list=label_list,
                            is_norm=is_norm)
    else:
        return [None, None, None, None]
