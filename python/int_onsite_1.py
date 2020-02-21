"""
Q. Write code to find out dependencies of a package and install them
E.g.
A -> B, C
B -> D, E, F
C -> F
D -> G
E -> G

Follow Up: What is the case if there are also package versions
Follow Up: DFS versus BFS

APPROACH-1:
DFS, go down the depth, install if not present and then come back up

APPROACH-2:
Decouple: method for handling discovery, and another to handle installation.
This enables separation of concern/orthogonality/compactness. Also enables us to test both functions independently.

"""

dependency = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G']
}


def install_package_dfs(package):
    installed = list()

    def _recurse(pkg):
        if pkg in installed:
            return

        if dependency.get(pkg):
            for dep in dependency[pkg]:
                if not dep in installed:
                    _recurse(dep)

        installed.append(pkg)
        print 'Install [{}]'.format(pkg)

    _recurse(package)


def install_package_bfs(package):
    def _get_dependencies(package):
        deps = list()
        queue = [package]
        deps.append(package)
        while queue:
            pkg = queue.pop(0)
            if dependency.get(pkg):
                for dep in dependency[pkg]:
                    queue.append(dep)
                    deps.append(dep)
        return deps[::-1]

    def _install_packages(package_list):
        installed = list()
        for pkg in package_list:
            if pkg not in installed:
                print 'Install [{}]'.format(pkg)
                installed.append(pkg)

    _install_packages(_get_dependencies(package))


##############

"""
Package Version info is present
"""


class Package(object):
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self):
        return '<{}:{}>'.format(self.name, self.version)


dependency_map = {
    'A': [Package('B', 1.0), Package('C', 1.0)],
    'B': [Package('D', 1.0), Package('E', 1.0), Package('F', 1.0)],
    'C': [Package('F', 1.1)],
    'D': [Package('G', 1.5)],
    'E': [Package('G', 1.0)]
}


# NOTE: If versions are specified, BFS is more faster.
# In case of DFS, an older version will be installed, and if a newer version is found, current installation needs to be upgraded
# With BFS, since we run the discovery first, newer version can be installed directly

def install_package_bfs_versions(package):
    def _get_dependencies(pkg):
        dependencies = list()
        queue = [pkg]

        while queue:
            p = queue.pop(0)
            if dependency_map.get(p):
                for dep in dependency_map[p]:
                    found = False
                    # if dependency is already found, upgrade the version to install if lower else nothing
                    for dep_found in dependencies:
                        if dep.name == dep_found.name:
                            if dep_found.version < dep.version:
                                dep_found.version = dep.version
                            found = True
                            break
                    # if dependency not found in the list, add it
                    if not found:
                        dependencies.append(dep)
                        queue.append(dep.name)

        return dependencies[::-1]

    def _install_packages(pacakges_list):
        for pkg in pacakges_list:
            print 'Install [{}]'.format(pkg)

    _install_packages(_get_dependencies(package))


if __name__ == '__main__':
    install_package_dfs('A')
    print '****'
    install_package_bfs('A')

    print '**************************'

    install_package_bfs_versions('A')
