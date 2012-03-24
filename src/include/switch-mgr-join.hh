/* Copyright 2009 (C) Nicira, Inc.
 *
 * This file is part of NOX.
 *
 * NOX is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NOX is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NOX.  If not, see <http://www.gnu.org/licenses/>.
 */
#ifndef SWITCH_MGR_JOIN_HH
#define SWITCH_MGR_JOIN_HH 1

#include "event.hh"
#include "netinet++/datapathid.hh"

namespace vigil {

/** \ingroup noxevents
 *
 * Switch_mgr_join_events are thrown for each new manager that connects to
 * NOX.
 *
 */

struct Switch_mgr_join_event
    : public Event
{
    Switch_mgr_join_event(datapathid id_) 
        : Event(static_get_name()), mgmt_id(id_) { }

    static const Event_name static_get_name() {
        return "Switch_mgr_join_event";
    }

    datapathid mgmt_id;

private:
    Switch_mgr_join_event(const Switch_mgr_join_event&);
    Switch_mgr_join_event& operator=(const Switch_mgr_join_event&);
};
    
} // namespace vigil

#endif /* switch-mgr-join.hh */
