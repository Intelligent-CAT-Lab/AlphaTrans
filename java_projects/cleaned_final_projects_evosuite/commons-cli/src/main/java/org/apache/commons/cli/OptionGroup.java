
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


package org.apache.commons.cli;

import java.io.Serializable;
import java.util.Collection;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;

/** A group of mutually exclusive options. */
public class OptionGroup implements Serializable {
    /** The serial version UID. */
    private static final long serialVersionUID = 1L;

    /** hold the options */
    private final Map<String, Option> optionMap = new LinkedHashMap<>();

    /** The name of the selected option */
    private String selected;

    /** specified whether this group is required */
    private boolean required;

    /**
     * Add the specified {@code Option} to this group.
     *
     * @param option the option to add to this group
     * @return this option group with the option added
     */
    public OptionGroup addOption(final Option option) {
        optionMap.put(option.getKey(), option);

        return this;
    }

    /**
     * @return the names of the options in this group as a {@code Collection}
     */
    public Collection<String> getNames() {
        return optionMap.keySet();
    }

    /**
     * @return the options in this group as a {@code Collection}
     */
    public Collection<Option> getOptions() {
        return optionMap.values();
    }

    /**
     * @return the selected option name
     */
    public String getSelected() {
        return selected;
    }

    /**
     * Tests whether this option group is required.
     *
     * @return whether this option group is required
     */
    public boolean isRequired() {
        return required;
    }

    /**
     * @param required specifies if this group is required
     */
    public void setRequired(final boolean required) {
        this.required = required;
    }

    /**
     * Set the selected option of this group to {@code name}.
     *
     * @param option the option that is selected
     * @throws AlreadySelectedException if an option from this group has already been selected.
     */
    public void setSelected(final Option option) throws AlreadySelectedException {
        if (option == null) {
            selected = null;
            return;
        }

        if (selected != null && !selected.equals(option.getKey())) {
            throw AlreadySelectedException.AlreadySelectedException1(this, option);
        }
        selected = option.getKey();
    }

    /**
     * Returns the stringified version of this OptionGroup.
     *
     * @return the stringified representation of this group
     */
    @Override
    public String toString() {
        final StringBuilder buff = new StringBuilder();

        final Iterator<Option> iter = getOptions().iterator();

        buff.append("[");

        while (iter.hasNext()) {
            final Option option = iter.next();

            if (option.getOpt() != null) {
                buff.append("-");
                buff.append(option.getOpt());
            } else {
                buff.append("--");
                buff.append(option.getLongOpt());
            }

            if (option.getDescription() != null) {
                buff.append(" ");
                buff.append(option.getDescription());
            }

            if (iter.hasNext()) {
                buff.append(", ");
            }
        }

        buff.append("]");

        return buff.toString();
    }
}
