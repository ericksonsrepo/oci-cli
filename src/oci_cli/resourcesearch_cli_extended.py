# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .generated import resourcesearch_cli
from . import cli_util
from . import json_skeleton_utils
import click

resourcesearch_cli.resource_summary_collection_group.commands.pop(resourcesearch_cli.search_resources.name)
resourcesearch_cli.resource_summary_collection_group.commands.pop(resourcesearch_cli.search_resources_structured_search_details.name)


@cli_util.copy_params_from_generated_command(resourcesearch_cli.search_resources_structured_search_details,
                                             params_to_exclude=['query'])
@resourcesearch_cli.resource_summary_collection_group.command(name='structured-search', help="""The SearchResources API allows you to search across all of your cloud infrastructure to find resources matching different criteria that you have permissions to access. Results may be across different types, and across compartments.""")
@cli_util.option('--query-text', required=True, help="""The structured query describing which resources to search for.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'resource_search', 'class': 'ResourceSummaryCollection'})
@cli_util.wrap_exceptions
def search_resources_structured_search_details(ctx, query_text, **kwargs):
    kwargs['query'] = query_text
    ctx.invoke(resourcesearch_cli.search_resources_structured_search_details, **kwargs)
