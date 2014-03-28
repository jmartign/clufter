# -*- coding: UTF-8 -*-
# Copyright 2014 Red Hat, Inc.
# Part of clufter project
# Licensed under GPLv2 (a copy included | http://gnu.org/licenses/gpl-2.0.txt)

ccs2needlexml = '''\
    <node>
        <xsl:for-each select="@*">
            <xsl:variable name="attr_name">
                <xsl:choose>
                    <!-- @nodeid -> @id -->
                    <xsl:when test="name() = 'nodeid'">
                        <xsl:value-of select="'id'"/>
                    </xsl:when>
                    <!-- @name -> @ring0_addr -->
                    <xsl:when test="name() = 'name'">
                        <xsl:value-of select="'ring0_addr'"/>
                    </xsl:when>
                    <!-- @votes -> @quorum_votes -->
                    <xsl:when test="name() = 'votes'">
                        <xsl:value-of select="'quorum_votes'"/>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:value-of select="''"/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:variable>
            <xsl:attribute name="{$attr_name}">
                <xsl:value-of select="."/>
            </xsl:attribute>
        </xsl:for-each>
        <xsl:if test="altname/@name">
            <xsl:attribute name="ring1_addr">
                <xsl:value-of select="altname/@name"/>
            </xsl:attribute>
        </xsl:if>
    </node>
'''

ccs2ccs_pcmk = '''\
    <clusternode name="{@name}" nodeid="{@nodeid}">
        <fence>
            <method name="pcmk-method">
                <device name="pcmk-redirect" port="{@name}"/>
            </method>
        </fence>
    </clusternode>
'''
