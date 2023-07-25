# ./tenantcalendar/dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:80bcd112b907ff044d191c4f0a6f1e95243d82cd
# Generated 2022-02-04 13:40:16.880325 by PyXB version 1.2.7-DEV using Python 3.10.2.final.0
# Namespace http://xml.homeinfo.de/schema/tenantcalendar

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    "urn:uuid:9b0ccbc0-85b7-11ec-aae0-7427eaa9df7d"
)

# Version of PyXB used to generate the bindings
_PyXBVersion = "1.2.7-DEV"
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    "http://xml.homeinfo.de/schema/tenantcalendar", create_if_missing=True
)
Namespace.configureCategories(["typeBinding", "elementBinding"])


def CreateFromDocument(
    xml_text, fallback_namespace=None, location_base=None, default_namespace=None
):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=fallback_namespace, location_base=location_base
    )
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}.
    """
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Complex type {http://xml.homeinfo.de/schema/tenantcalendar}Events with content type ELEMENT_ONLY
class Events(pyxb.binding.basis.complexTypeDefinition):
    """
    Kunden-Events.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Events")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 22, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "event"),
        "event",
        "__httpxml_homeinfo_deschematenantcalendar_Events_event",
        True,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 29, 12
        ),
    )

    event = property(
        __event.value,
        __event.set,
        None,
        "\n                        Die einzelnen Kunden-Events.\n                    ",
    )

    _ElementMap.update({__event.name(): __event})
    _AttributeMap.update({})


_module_typeBindings.Events = Events
Namespace.addCategoryObject("typeBinding", "Events", Events)


# Complex type {http://xml.homeinfo.de/schema/tenantcalendar}Event with content type ELEMENT_ONLY
class Event(pyxb.binding.basis.complexTypeDefinition):
    """
    Ein Event.
    """

    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, "Event")
    _XSDLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 40, 4
    )
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "title"),
        "title",
        "__httpxml_homeinfo_deschematenantcalendar_Event_title",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 47, 12
        ),
    )

    title = property(
        __title.value,
        __title.set,
        None,
        "\n                        Titel des Events.\n                    ",
    )

    # Element text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "text"),
        "text",
        "__httpxml_homeinfo_deschematenantcalendar_Event_text",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 54, 12
        ),
    )

    text = property(
        __text.value,
        __text.set,
        None,
        "\n                        Fließtext des Events.\n                    ",
    )

    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "start"),
        "start",
        "__httpxml_homeinfo_deschematenantcalendar_Event_start",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 61, 12
        ),
    )

    start = property(
        __start.value,
        __start.set,
        None,
        "\n                        Beginn des Events.\n                    ",
    )

    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(None, "end"),
        "end",
        "__httpxml_homeinfo_deschematenantcalendar_Event_end",
        False,
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 68, 12
        ),
    )

    end = property(
        __end.value,
        __end.set,
        None,
        "\n                        Ende des Events.\n                    ",
    )

    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "id"),
        "id",
        "__httpxml_homeinfo_deschematenantcalendar_Event_id",
        pyxb.binding.datatypes.nonNegativeInteger,
    )
    __id._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 76, 8
    )
    __id._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 76, 8
    )

    id = property(
        __id.value,
        __id.set,
        None,
        "\n                    Datenbank-ID des Events.\n                ",
    )

    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "created"),
        "created",
        "__httpxml_homeinfo_deschematenantcalendar_Event_created",
        pyxb.binding.datatypes.dateTime,
    )
    __created._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 83, 8
    )
    __created._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 83, 8
    )

    created = property(
        __created.value,
        __created.set,
        None,
        "\n                    Erstellungsdatum des Events.\n                ",
    )

    # Attribute modified uses Python identifier modified
    __modified = pyxb.binding.content.AttributeUse(
        pyxb.namespace.ExpandedName(None, "modified"),
        "modified",
        "__httpxml_homeinfo_deschematenantcalendar_Event_modified",
        pyxb.binding.datatypes.dateTime,
    )
    __modified._DeclarationLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 90, 8
    )
    __modified._UseLocation = pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 90, 8
    )

    modified = property(
        __modified.value,
        __modified.set,
        None,
        "\n                    Letzte Änderung des Events.\n                ",
    )

    _ElementMap.update(
        {
            __title.name(): __title,
            __text.name(): __text,
            __start.name(): __start,
            __end.name(): __end,
        }
    )
    _AttributeMap.update(
        {__id.name(): __id, __created.name(): __created, __modified.name(): __modified}
    )


_module_typeBindings.Event = Event
Namespace.addCategoryObject("typeBinding", "Event", Event)


events = pyxb.binding.basis.element(
    pyxb.namespace.ExpandedName(Namespace, "events"),
    Events,
    documentation="\n                Wurzelelement.\n            ",
    location=pyxb.utils.utility.Location(
        "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 13, 4
    ),
)
Namespace.addCategoryObject("elementBinding", events.name().localName(), events)


Events._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "event"),
        Event,
        scope=Events,
        documentation="\n                        Die einzelnen Kunden-Events.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 29, 12
        ),
    )
)


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(
        min=0,
        max=None,
        metadata=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 29, 12
        ),
    )
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        Events._UseForTag(pyxb.namespace.ExpandedName(None, "event")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 29, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Events._Automaton = _BuildAutomaton()


Event._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "title"),
        pyxb.binding.datatypes.string,
        scope=Event,
        documentation="\n                        Titel des Events.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 47, 12
        ),
    )
)

Event._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "text"),
        pyxb.binding.datatypes.string,
        scope=Event,
        documentation="\n                        Fließtext des Events.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 54, 12
        ),
    )
)

Event._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "start"),
        pyxb.binding.datatypes.dateTime,
        scope=Event,
        documentation="\n                        Beginn des Events.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 61, 12
        ),
    )
)

Event._AddElement(
    pyxb.binding.basis.element(
        pyxb.namespace.ExpandedName(None, "end"),
        pyxb.binding.datatypes.dateTime,
        scope=Event,
        documentation="\n                        Ende des Events.\n                    ",
        location=pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 68, 12
        ),
    )
)


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Event._UseForTag(pyxb.namespace.ExpandedName(None, "title")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 47, 12
        ),
    )
    st_0 = fac.State(
        symbol,
        is_initial=True,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Event._UseForTag(pyxb.namespace.ExpandedName(None, "text")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 54, 12
        ),
    )
    st_1 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        Event._UseForTag(pyxb.namespace.ExpandedName(None, "start")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 61, 12
        ),
    )
    st_2 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Event._UseForTag(pyxb.namespace.ExpandedName(None, "end")),
        pyxb.utils.utility.Location(
            "/home/neumann/Projekte/tenantcalendar/tenantcalendar.xsd", 68, 12
        ),
    )
    st_3 = fac.State(
        symbol,
        is_initial=False,
        final_update=final_update,
        is_unordered_catenation=False,
    )
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, []))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, []))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, []))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Event._Automaton = _BuildAutomaton_()
