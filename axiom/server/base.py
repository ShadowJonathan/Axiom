import abc

# do not import axiom.network, cyclic dependency


class MatrixHomeServer(abc.ABC):
    """This class mainly acts to define the signatures any network XService will use."""
