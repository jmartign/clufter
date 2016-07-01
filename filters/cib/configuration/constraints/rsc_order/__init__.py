# -*- coding: UTF-8 -*-
# Copyright 2016 Red Hat, Inc.
# Part of clufter project
# Licensed under GPLv2+ (a copy included | http://gnu.org/licenses/gpl-2.0.txt)
__author__ = "Jan Pokorný <jpokorny @at@ Red Hat .dot. com>"

from ....filters._2pcscmd import verbose_ec_test, verbose_inform
from ....utils_xslt import NL, xslt_is_member

cib2pcscmd_options = (
    'symmetrical',
    'score',
    'kind',
)

cib2pcscmd = ('''\
    <xsl:choose>
        <!-- plain first-then -->
        <xsl:when test="@first and @then">
''' + (
            verbose_inform('"new order constraint: ", @id')
) + '''
            <xsl:value-of select="concat($pcscmd_pcs, 'constraint order')"/>
            <xsl:if test="@first-action and @first-action != 'start'">
                <xsl:value-of select="concat(' ', @first-action)"/>
            </xsl:if>
            <xsl:value-of select="concat(' ', @first, ' then')"/>
            <xsl:if test="@then-action and @then-action != 'start'">
                <xsl:value-of select="concat(' ', @then-action)"/>
            </xsl:if>
            <xsl:value-of select="concat(' ', @then)"/>
            <xsl:for-each select="@*[
''' + (
                xslt_is_member('name()', cib2pcscmd_options)
) + ''']">
                <xsl:value-of select="concat(' ', name(), '=', .)"/>
            </xsl:for-each>
            <xsl:value-of select="concat(' ', 'id=', @id)"/>
            <xsl:value-of select="'%(NL)s'"/>
''' + (
            verbose_ec_test
) + '''
        </xsl:when>

        <!-- resource sets -->
        <xsl:when test="resource_set">
            <xsl:message
            >WARNING: order constraint with resource sets not supported (yet)</xsl:message>
        </xsl:when>
    </xsl:choose>

''') % dict(
    NL=NL,
)
