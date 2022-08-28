def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    
    return getOrgInfo(topManager,reportOne,reportTwo).lowest_common_manager

def getOrgInfo(manager, reportOne, reportTwo):
    num_important_reports = 0
    for directReport in manager.directReports:
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
        if orgInfo.lowest_common_manager is not None:
            return orgInfo
        num_important_reports += orgInfo.num_important_reports
    if manager == reportOne or manager == reportTwo:
        num_important_reports += 1
    lowest_common_manager = manager if num_important_reports == 2 else None
    return OrgInfo(lowest_common_manager, num_important_reports)
    
    
class OrgInfo:
    def __init__(self,lowest_common_manager,num_important_reports):
        self.lowest_common_manager = lowest_common_manager
        self.num_important_reports = num_important_reports
    


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
