# -*- coding: utf-8 -*-

from datetime import datetime
from protoLib.utilsBase import stripAccents

PROTO_PREFIX = "prototype.ProtoTable."

def baseDefinition( pEntity , entityName, viewTitle  ):
    """ protoEntity: Es la traza de la generacion del protipo  dominio.modelo.entidad  
    """ 
    
    viewName   = stripAccents( viewTitle  )

    return  {
    "__ptType": "pcl",
    "protoConcept": "prototype.ProtoTable",
    "protoOption" : PROTO_PREFIX + viewName,
    "protoEntity" : entityName,  
    "protoEntityId" : pEntity.id,  
    "description" : pEntity.description ,
    "jsonField"   : "info" ,
    "protoIcon"   : "icon-1",
    "shortTitle"  : viewTitle,
    "updateTime"  : datetime.now(),
    "metaVersion" : "13.0224",
    "idProperty"  : "id",
    "fields": [
        {
            "name": "id",
            "readOnly": True,
            "hidden": True,
            "type": "autofield"
        },
        {
            "name": "entity",
            "readOnly": True,
            "hidden": True,
            "defaultValue" : entityName, 
        },
        {
            "name": "info",
            "searchable": True,
            "readOnly": True,
            "hidden": True,
            "type": "text",
        },               
        {
            "zoomModel": "auth.User",
            "name": "smOwningUser",
#            "fkId": "smOwningUser_id",
            "readOnly": True,
            "type": "foreigntext"
        },
        {
            "name": "smModifiedOn",
            "readOnly": True,
            "type": "datetime"
        },
#        {
#            "fkField": "smCreatedBy",
#            "name": "smCreatedBy_id",
#            "readOnly": True,
#            "hidden": True,
#            "type": "foreignid"
#        },
#        {
#            "fkField": "smOwningUser",
#            "name": "smOwningUser_id",
#            "readOnly": True,
#            "hidden": True,
#            "type": "foreignid"
#        },
        {
            "zoomModel": "protoLib.TeamHierarchy",
            "name": "smOwningTeam",
#            "fkId": "smOwningTeam_id",
            "readOnly": True,
            "type": "foreigntext"
        },
        {
            "name": "smCreatedOn",
            "readOnly": True,
            "type": "datetime"
        },
        {
            "zoomModel": "auth.User",
            "name": "smModifiedBy",
#            "fkId": "smModifiedBy_id",
            "readOnly": True,
            "type": "foreigntext"
        },
        {
            "name": "smRegStatus",
            "readOnly": True,
            "type": "string"
        },
        {
            "zoomModel": "auth.User",
            "name": "smCreatedBy",
#            "fkId": "smCreatedBy_id",
            "readOnly": True,
            "type": "foreigntext"
        },
#        {
#            "fkField": "smOwningTeam",
#            "name": "smOwningTeam_id",
#            "readOnly": True,
#            "hidden": True,
#            "type": "foreignid"
#        },
#        {
#            "fkField": "smModifiedBy",
#            "name": "smModifiedBy_id",
#            "readOnly": True,
#            "hidden": True,
#            "type": "foreignid"
#        },
        {
            "name": "smWflowStatus",
            "readOnly": True,
            "type": "string"
        }
    ],
    "protoDetails": [],
    "gridConfig": {
        "listDisplay": [],
        "baseFilter": [],
        "searchFields": [ "info",],
        "sortFields": [],
        "hiddenFields": [ "id", "info", "entity" ],
        "readOnlyFields": [],
    },
    "protoForm": {
        "__ptType": "protoForm",
        "items": [
            {
                "__ptType": "fieldset",
                "fsLayout": "2col",
                "items": []
            },
            {
                "__ptType": "fieldset",
                "collapsible": True,
                "title": "Admin",
                "collapsed": True,
                "fsLayout": "2col",
                "items": [
                    {
                        "__ptType": "formField",
                        "name": "smOwningUser"
                    },
                    {
                        "__ptType": "formField",
                        "name": "smOwningTeam"
                    },
                    {
                        "__ptType": "formField",
                        "name": "smModifiedBy"
                    },
                    {
                        "__ptType": "formField",
                        "name": "smCreatedBy"
                    },
                    {
                        "__ptType": "formField",
                        "name": "smModifiedOn"
                    },
                    {
                        "__ptType": "formField",
                        "name": "smCreatedOn"
                    },
                    {
                        "__ptType": "formField",
                        "name": "smRegStatus"
                    },
                    {
                        "__ptType": "formField",
                        "name": "smWflowStatus"
                    }
                ]
            }
        ]
    }
}    