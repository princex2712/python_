# Python: Get a list of locally installed Python modules
import pkg_resources

installed = pkg_resources.working_set
installed_list = sorted(["%s==%s" %(i.key,i.version) for i in installed])

for module in installed_list:
    print(module)