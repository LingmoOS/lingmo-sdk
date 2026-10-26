// SPDX-FileCopyrightText: 2026 LingmoOS Contributors
// SPDX-License-Identifier: GPL-3.0-or-later

// The toolkit's declarations live in Lingmo::Base, Lingmo::Base::DBus,
// Lingmo::UI and Lingmo::I18n. The desktop's sources, ported from the
// Cutefish toolkit, spell them base::, dbus::, ui:: and i18n::, and some of
// them the Lingmo:: names in their lower-case form. This header aliases the
// spellings so either way compiles.
//
// The toolkit's CMake target force-includes it, so it comes before any
// header that relies on the names, without every source having to include
// it: the target's interface carries -include base/compat.h.
#pragma once

#ifdef __cplusplus

namespace Lingmo::Base {}
namespace Lingmo::Base::DBus {}
namespace Lingmo::UI {}
namespace Lingmo::I18n {}

namespace Lingmo {
namespace base = Base;
namespace ui = UI;
namespace dbus = Base::DBus;
namespace i18n = I18n;
} // namespace Lingmo

// base::dbus:: is how the sources nest the bus classes inside base.
namespace Lingmo::Base {
namespace dbus = DBus;
} // namespace Lingmo::Base

namespace base = Lingmo::Base;
namespace dbus = Lingmo::Base::DBus;
namespace ui = Lingmo::UI;
namespace i18n = Lingmo::I18n;

#endif // __cplusplus
