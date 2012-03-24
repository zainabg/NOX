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
#ifndef PYDATA_CACHE_HH
#define PYDATA_CACHE_HH 1

#include <Python.h>

#include "datacache.hh"
#include "component.hh"

namespace vigil {
namespace applications {

class PyData_cache {
public:
    PyData_cache(PyObject*);

    void configure(PyObject*);

    int64_t get_authenticated_id(PrincipalType ptype) const;
    int64_t get_unauthenticated_id(PrincipalType ptype) const;
    int64_t get_unknown_id(PrincipalType ptype) const;

    const std::string& get_authenticated_name() const;
    const std::string& get_unauthenticated_name() const;
    const std::string& get_unknown_name() const;

    const std::string& get_name(PrincipalType type, int64_t id) const;

private:
    Data_cache *data_cache;
    container::Component* c;
};

}
}

#endif
